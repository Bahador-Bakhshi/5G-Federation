graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 3
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 14
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 91
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 127
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 66
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 97
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 110
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 157
  ]
]
