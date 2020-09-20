graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 13
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 2
    memory 5
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 9
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 158
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 60
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 71
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 78
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 171
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 124
  ]
]
