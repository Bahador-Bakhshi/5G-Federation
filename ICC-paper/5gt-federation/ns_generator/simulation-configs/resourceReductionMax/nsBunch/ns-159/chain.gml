graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 2
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 2
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 9
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 191
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 182
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 98
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 180
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 172
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 181
  ]
]
