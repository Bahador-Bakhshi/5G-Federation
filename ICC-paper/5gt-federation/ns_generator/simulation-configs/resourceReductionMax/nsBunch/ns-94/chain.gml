graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 6
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 4
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 90
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 92
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 157
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 182
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 119
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 152
  ]
]
