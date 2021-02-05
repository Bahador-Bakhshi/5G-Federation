graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 16
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 16
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 16
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 186
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 78
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 70
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 134
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 62
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 89
  ]
]
