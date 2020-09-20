graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 9
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 16
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 123
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 169
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 198
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 65
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 101
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 74
  ]
]
