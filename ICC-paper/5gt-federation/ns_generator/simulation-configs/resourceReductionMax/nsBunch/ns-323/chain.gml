graph [
  node [
    id 0
    label 1
    disk 6
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 5
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 10
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 7
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 125
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 171
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 154
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 156
  ]
  edge [
    source 2
    target 5
    delay 29
    bw 75
  ]
]
