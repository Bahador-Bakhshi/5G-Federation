graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 3
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 3
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 10
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
    bw 143
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 126
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 99
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 123
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 99
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 133
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 120
  ]
]
