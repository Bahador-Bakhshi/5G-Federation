graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 16
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 2
    memory 11
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 137
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 171
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 200
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 152
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 182
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 109
  ]
]
