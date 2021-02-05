graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 2
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 1
    memory 1
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 79
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 54
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 73
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 65
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 56
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 86
  ]
]
