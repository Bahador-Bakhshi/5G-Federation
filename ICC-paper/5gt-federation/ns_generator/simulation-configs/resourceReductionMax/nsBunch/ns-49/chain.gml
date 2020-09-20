graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 8
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
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 2
    memory 13
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 77
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 128
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 174
  ]
  edge [
    source 0
    target 3
    delay 34
    bw 59
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 86
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 90
  ]
]
