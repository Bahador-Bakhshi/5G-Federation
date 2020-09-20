graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 10
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 104
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 87
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 61
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 171
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 55
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 117
  ]
]
